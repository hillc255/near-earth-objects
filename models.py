"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object,
    such as its primary designation (required, unique), IAU name (optional),
    diameter in kilometers (optional - sometimes unknown), and whether it's
    marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to
                     the constructor.
        :param designation: The primary designation for this NearEarthObject.
        :param name: The IAU name for this NearEarthObject.
        :param diameter: The diameter, in kilometers, of this NearEarthObject.
        :param hazardous: Whether or not this NearEarthObject is potentially
                          hazardous.
        :param approaches: A collection of this NearEarthObjects close
                           approaches to Earth.
        """

        self.designation = info.get("designation")
        self.name = info.get("name")
        self.diameter = info.get("diameter")
        self.hazardous = info.get("hazardous")

        # Create an empty initial collection of linked approaches.
        self.approaches = []

        if not self.diameter:
            self.diameter = float("nan")
        else:
            self.diameter = float(self.diameter)

        if self.hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        if not self.name:
            self.name = None

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        return f'{self.designation} ({self.name})' if self.name else \
            f'{self.designation}'

    def __str__(self):
        """Return `str(self)`."""

        if self.hazardous is True:
            neo_hazard = 'is'
        else:
            neo_hazard = 'is not'
        return f"A NearEarthObject {self.fullname} has a diameter of "\
            f"{self.diameter} km and {neo_hazard} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
        this object."""
        return f"NearEarthObject(designation={self.designation!r}, "\
            f"name={self.name!r}, diameter={self.diameter:.3f}, "\
            f"hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close
    approach to Earth, such as the date and time (in UTC) of closest approach,
    the nominal approach distance in astronomical units, and the relative
    approach velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        # Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and
        # `velocity`.

        # designation code pdes
        self._designation = info.get('designation')
        self.time = info.get('time')
        self.distance = info.get('distance')
        self.velocity = info.get('velocity')

        # Create an attribute for the referenced NEO, originally None.
        self.neo = info.get('neo')

        # Function for time and data type for distance, velocity
        # and cd_to_datetime function for this attribute.
        if self.time:
            self.time = cd_to_datetime(self.time)
        # dist - if distance else float('nan')
        if not self.distance:
            self.distance = float("nan")
        else:
            self.distance = float(self.distance)
        # v_rel - if velocity else float('nan')
        if not self.velocity:
            self.velocity = float("nan")
        else:
            self.velocity = float(self.velocity)

    @property
    def designation(self):
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't exist
        in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        if self.time:
            return datetime_to_str(self.time)
        return "unknown approach time"

        """Return a representation of the full name of this NEO."""

    def __str__(self):
        """Return `str(self)`."""

        return f"A CloseApproach at {self.time_str}, {self.neo.fullname} "\
            f"approaches Earth at a distance of {self.distance} au and a "\
            f"velocity of {self.velocity} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
        this object."""
        return f"CloseApproach(time={self.time_str!r}, "\
               f"distance={self.distance:.2f}, "\
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
