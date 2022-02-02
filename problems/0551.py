"551. Student Attendance Record I"

# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Input: s = "PPALLP" / Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

# Input: s = "PPALLL" / Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

class Solution:
    def checkRecord(self, s: str) -> bool:

        return True if s.count('A') < 2 and 'LLL' not in s else False
