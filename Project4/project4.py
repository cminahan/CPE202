""" Project 4:
Name: Claire Minahan
Course: CPE202-03
Instructor: Kuboi
"""

import os
import math
from hashtables import *

class SearchEngine:
    """ builds and maintains an inverted index of documents
        stored in a specified directory
    Attributes:
        directory(str): a directory name
        stopwords(HashMap): a hash table containing stop words
        doc_length(HashMap): a hash map containing the total
                            number of words in each document
        term_freqs(HashMap): a hash table of hash tables
    """

    def __init__(self, directory, stopwords):
        self.dir = directory
        self.stopwords = stopwords
        self.doc_length = HashTableLinear()  # key: file_path_name, val: number of words
        self.term_freqs = HashTableLinear()  # key: word, val: another HashMap
        self.index_files(self.dir)

    def __repr__(self):
        return "Terms: %s" %(self.term_freqs)

    def __eq__(self, other):
        return isinstance(other, SearchEngine) \
               and self.dir == other.dir \
               and self.stopwords == other.stopwords \
               and self.doc_length == other.doc_length \
               and self.term_freqs == other.term_freqs

    def read_file(self, infile):
        """ a helper function to read a file
        Args:
            infile(str): the path to a file
        Returns:
            list: a list of str read from file
        """
        with open(infile, 'r') as fin:
            string = fin.read()
            file = string.split()
        return file

    def parse_words(self, lines):
        """ splits strings into words by spaces
        Converts words to lower case,
        and removes newline chars, parentheses, brackets such as "[]", "{}"
        and punctuation such as ",", ".", "?", "!".
        You may use replace() and other built in string functions
        Excludes stopwords.
        Args:
            lines(list): a list of strings
        Returns:
            list: a list of words
        """
        new_list = []
        for string in lines:
            list_string = string.split()
            if len(list_string) > 1:
                for word in list_string:
                    new_word = word.lower()
                    if not new_word.isalpha():
                        other_word = ''
                        for char in new_word:
                            if 97 <= ord(char) <= 122:
                                other_word += char
                        new_word = other_word
                    new_list.append(new_word)
            else:
                new_string = string.lower()
                if not new_string.isalpha():
                    newer_word = ''
                    for char in new_string:
                        if 97 <= ord(char) <= 122:
                            newer_word += char
                    new_string = newer_word
                new_list.append(new_string)
        new_list = self.exclude_stopwords(new_list)
        return new_list

    def exclude_stopwords(self, terms):
        """ exclude stopwords from the list of terms
        Args:
            terms(list): a list of words
        Returns:
            list: a list of str with stopwords removed
        """
        new_terms = []
        for word in terms:
            if not self.stopwords.contains(word):
                new_terms.append(word)
        return new_terms

    def count_words(self, file_path_name, words):
        """ count words in a file and stores the frequency of each
        word in the term_freqs hash table. The key of the term_freqs
        hash table shall be words. The values of the term_freqs hash
        table shall be hash tables (term_freqs is a hash table of hash
        tables). The keys of the hash tables(inner hash tables) stored
        in the terms_freqs shall be file names. The values of the
        inner hash tables shall be the frequencies of words. For
        example, self.term_freqs[word][file_path_name]+=1;
        Words should not contain stopwords.
        Also store the total count of words contained in the file
        in the doc_length hash table.
        Args:
            file_path_name(str): the file name
            words(list): a list of words
        """
        for word in words:
            if word in self.term_freqs:
                if file_path_name in self.term_freqs[word]:
                    self.term_freqs[word][file_path_name] += 1
                else:
                    self.term_freqs[word][file_path_name] = 1
            else:
                inner_hash = HashTableLinear()
                #inner_hash.put(file_path_name, 1)
                #self.term_freqs.put(word, inner_hash)
                self.term_freqs[word] = inner_hash
                self.term_freqs[word][file_path_name] = 1
        self.doc_length.put(file_path_name, len(words))

    def index_files(self, directory):
        """ index all text files in a given directory
        Args:
            directory(str): the path of the directory
        """
        list_file = os.listdir(directory)
        for item in list_file:
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                parts = os.path.splitext(item)
                if parts[1] == '.txt':
                    lines = self.read_file(path)
                    words = self.parse_words(lines)
                    self.count_words(path, words)

    def get_wf(self, term_freq):
        """ competes the weighted frequency
        Args:
            term_freq(float): term frequency
        Returns:
            float: the weighted frequency
        """
        if term_freq > 0:
            weighted_freq = 1 + math.log(term_freq)
        else:
            weighted_freq = 0
        return weighted_freq

    def get_scores(self, terms):
        """ creates a list of scores for each file in corpus
        The score = weighted frequency / the total word count in the file
        Compute this score for each term in a query and sum all the scores
        Args:
            terms(list): a list of str
        Returns:
            list: a list of tuples, each containing the file_path_name
            and its relevancy score
        """
        # pseudo code
        # scores = HashMap()
        # For each query term t
        #   Fetch a hash table of t from self.term_freqs
        #   For each line in the hash table, add wf to scores[file]
        # For each file in scores, do scores[file]/=self.doc_length[file]
        # Return scores
        scores = HashTableLinear()
        for query in terms:
            hash_table = self.term_freqs.get(query)
            keys = hash_table.keys()
            for file in keys:
                term_freq = hash_table.get(file)
                weighted_freq = self.get_wf(term_freq)
                if scores.contains(file):
                    scores[file] += weighted_freq
                else:
                    scores[file] = weighted_freq
        score_keys = scores.keys()
        score_tuple = []
        for file in score_keys:
            scores[file] /= self.doc_length[file]
            tup = (file, (scores[file]))
            score_tuple.append(tup)
        return score_tuple

    def rank(self, scores):
        """ ranks files in descending order of relevancy
        Args:
            scores(list): a list of tuples:(file_path_name,score)
        Returns:
            list: a list of tuples:(file_path_name, score) sorted
            in descending order of relevancy
        """
        size = len(scores)
        end_index = size - 1
        new_list = []
        for num in range(size):
            max_index = 0
            for index in range(size):
                if scores[index] > scores[max_index] and index <= end_index:
                    max_index = index
            new_list.append(scores[max_index])
            scores.pop(max_index)
            end_index -= 1
            size -= 1
        return new_list

    def search(self, query):
        """ search for the query terms in files
        Args:
            query(str): query input e.g."computer science"
        Returns:
            list: a list of tuples(file_name, score) sorted
            in descending order or relevancy
            excluding files whose relevancy score is 0
        """
        words = self.parse_words([query])
        new_hash = HashTableLinear()
        for word in words:
            new_hash.put(word, 0)
        keys = new_hash.keys()
        scores = self.get_scores(keys)
        return self.rank(scores)


def main():
    """ The driver of the program
    1. It asks the user to input the path of the directory
        containing documents
    2. It creates an object of SearchEngine importing stop
        words, and builds an inverted index on the documents
    3. It asks the user to input a search query (keywords
        separated by space: eg. "computer science"
    4. The user must prepend "s:" to a query indicating
        that the user wants to do search. The user must
        type ":q" if they wants to quit
    5. It searches for documents containing any of the
        keywords using the search() method. The method is
        going to return a list of tuples(file_path_name, score)
    6. It shows a list of files (including their paths) containing
        the keywords in descending order of relevancy. You may
        create helper function / method for printing the list
        of files nicely on the screen
    7. Until the user types "q:" for quitting, it keeps asking
        the user to enter a new query
    """
    directory = input("Input the path of the directory containing documents: ")
    stopwords = import_stopwords("stop_words.txt")
    engine = SearchEngine(directory, stopwords)
    #print(engine.term_freqs)
    query = input('Input a search query (prepend "s:" to do a search, ":q" to quit): ')
    while query.find(":q") == -1:
        query = query[2:]
        result = engine.search(query)
        for file in result:
            print(file[0])
            print(file[1])
        query = input('Input a search query (prepend "s:" to do a search, ":q" to quit): ')


if __name__ == '__main__':
    main()
