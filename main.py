class Tally:
    def __init__(self, numberlist=None, numbertuple=None):
        self.numberlist = numberlist
        self.numbertuple = numbertuple
        if numberlist is None:
            pass
        if numbertuple is None:
            pass

    @staticmethod
    def plus(tuplefirst, tuplesecond, pluslist=None):
        """
        After ensuring that the number of elements in two tuples is the same, the two tuples are converted into a list.
        Finally, the two elements and subscript elements are added to the list and returned.
        """
        if pluslist is None:
            pluslist = []
        tuplefirst = list(tuplefirst)
        tuplesecond = list(tuplesecond)
        if len(tuplefirst) == len(tuplesecond):
            for i, _ in zip(tuplefirst, tuplesecond):
                pluslist.append(i + _)
        else:
            raise ValueError('Two tuples\'s number is not agreement')
        return pluslist

    @staticmethod
    def minus(tuplefirst, tuplesecond, minuslist=None):
        """
        After ensuring that the number of elements in two tuples is the same, the two tuples are converted into a
        list, and finally the two elements are subtracted from the subscript elements and added to the list to return.
        """
        if minuslist is None:
            minuslist = []
        tuplefirst = list(tuplefirst)
        tuplesecond = list(tuplesecond)
        if len(tuplefirst) == len(tuplesecond):
            for i, _ in zip(tuplefirst, tuplesecond):
                if i >= _:
                    minuslist.append(i - _)
                else:
                    minuslist.append(_ - i)
        else:
            raise ValueError('Two tuples\'s number is not agreement')
        return minuslist

    @staticmethod
    def times(self, tuplesecond, timeslist=None):
        """
        To ensure that the number of two tuple elements is same as below, convert two tuples into lists, and finally
        multiply two elements with subscript elements and add them to the list.
        """
        if timeslist is None:
            timeslist = []
        tuplesecond = list(tuplesecond)
        if len(self) == len(tuplesecond):
            for i, _ in zip(self, tuplesecond):
                timeslist.append(i * _)
        else:
            raise ValueError('Two tuples\'s number is not agreement')
        return timeslist
