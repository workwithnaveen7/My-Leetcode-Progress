# Last updated: 4/18/2025, 11:30:12 PM
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year=bin(int(date[:4]))[2:]
        month=bin(int(date[5:7]))[2:]
        day=bin(int(date[8:10]))[2:]
        ans=year+'-'+month+'-'+day
        return "".join(ans)