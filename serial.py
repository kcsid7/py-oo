"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __repr__(self):
        """Representation"""
        return f"<SerialGenerator start=100 next=101>"

    def __init__(self,start=0):
        """Generator initialization, starts at 0"""
        self.start = start
        self.next = start
    
    def generate(self):
        """Return the next incremental value"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Reset the number to start"""
        self.next = self.start

