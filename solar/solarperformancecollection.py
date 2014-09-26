"""
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
        """ Return a dictionary of performance (values) by systems (keys) for the top k systems

        usage:
        systemperformance = spc.top(10)

        where systemperformance = {'Sleepy': 1.01,
                                   'Drowsy': 1.10,
                                   ...
                                  }
        """
        pass
