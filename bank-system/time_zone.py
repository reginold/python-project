
import numbers
from datetime import timedelta

class TimeZone:

    def __init__(self, name, offset_hours, offset_minutues):
        """
        Include two instance attributes, offset and name as read-only properties.
        """
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Timezone name cannot be empty.")

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError("Hour offset must be an integer.")

        if not isinstance(offset_minutues, numbers.Integral):
            raise ValueError("Minute offset must be an integer.")

        if offset_minutues> 59 or offset_minutues < -59:
            raise ValueError("Minutes ofset must be between -59 and 59(inclusive).")

        # offsets are technically bounded between -12:00 and 14:00
        # see: https://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        offset = timedelta(hours=offset_hours, minutes=offset_minutues)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("Offset must be betweern -12:00 and +14:00.")
        
        self._offset_hour = offset_hours
        self._off_minutes = offset_minutues
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hour == other.offset_hours and
                self._off_minutes == other.offset_minutues)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")

# test

# tz1 = TimeZone('ABC', -2, -15)
# print(tz1.name)
# # tz2 = TimeZone('', -2, -15)
# # print(tz2.name)
# tz2 = TimeZone('ABC', -2, -15)
# print(tz2.offset)
# tz2 = TimeZone('ABC', -3, 18)
# print(tz2.offset)

# from datetime import datetime

# dt = datetime.utcnow()
# print(dt)
# print(dt + tz1.offset)