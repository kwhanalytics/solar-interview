"""
SolarPerformanceColleciton is a dataset to hold system production data.
It is designed to be efficient, both in time and storage space.
"""

class SolarPerformanceCollection(object):
    """
    """

    def __init__(self):
        """
        """

    def add(self, system):
        """ ADD a system to the collection

        usage:
            system = SolarPerformance('Sleepy')
            spc = SolarPerformanceCollection()
            spc.add(system)
        """

    def count(self):
        """
        """

    def max(self):
        """
        """

    def min(self):
        """
        """

    def percentile(self,pct):
        """ Calculate the nth percentile of the data collection

        usage:
        tenthpercentileperformance = spc.percentile(10)
        """
        pass

    def top(self, k):
        """ Return an array of dictionaries of performance
        (lifetimeperformance) and names (systemname) for the top k systems.
        The results should be ordered in descending order.

        usage:
        systemperformance = spc.top(10)

        where systemperformance = [
                {'systemname': 'Sleepy', 'lifetimeperformance': 1.10},
                {'systemname': 'Doc', 'lifetimeperformance': 1.08,
                ...
            ]
        """
        pass
