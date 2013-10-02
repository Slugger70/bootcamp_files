import string

class InvalidBaseException(Exception):
    pass

class nucleotide_sequence:
    '''The base class for all nucleotide sequences.'''
    '''revcom is the complementarity matrix for regular nucleotide sequences'''
    
    def __init__(self, sequence):
        assert len(sequence) > 0
        '''The constructor: accepts a nucleotide sequence'''
        if set(sequence).difference(set(self.valid)) != set():
            raise InvalidBaseException("The sequence contains invalid characters. " + ''.join(set(sequence).difference(set(self.valid))))
        self.sequence = sequence
        self.basecounts = {}
        
    def base_count(self, base):
        assert base in set("ACTGU")
        '''base_count function: accepts a nucleotide base and returns the count of that base in the sequence'''
        if base in self.basecounts:
            return self.basecounts[base]
        else:
            self.basecounts[base] = self.sequence.count(base)
            return self.basecounts[base]
        
    def gc_content(self):
        '''gc_content: returns the gc content of the sequence as a fraction (float)'''
        assert len(self.sequence) > 0
        return (self.base_count("G") + self.base_count("C"))/float(len(self.sequence))
        
    def reverse_complement(self):
        '''reverse_complement: returns the reverse complement of the sequence using the complementarity matrix (revcom).
        returns a sequence.'''
        result = ""
        for i in self.sequence:
            result += self.revcom[i]
        return result[::-1]
 
class DNA_sequence(nucleotide_sequence):
     '''A seequence class for DNA sequences (no IUPAC codes.)'''
     revcom = {"A":"T", "T":"A", "G":"C", "C":"G"}
     valid = set(revcom)
     def __init__(self,sequence):
        nucleotide_sequence.__init__(self,sequence)        
    

class RNA_sequence(nucleotide_sequence):
    '''A Sequence class for RNA sequences (U instead of T) - (no IUPAC codes.)'''
    revcom = {"A":"U", "U":"A", "G":"C", "C":"G"}
    valid = set(revcom)
    def __init__(self,sequence):
        nucleotide_sequence.__init__(self,sequence)
        
