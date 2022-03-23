"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member: dict):
        # fill this method and update the return
        if "id" in member:
            self._members.append(member)
        else:
            member["id"] = self._generateId()
            self._members.append(member)

    def delete_member(self, id: int):
        # fill this method and update the return
        filtered_members = list(
            filter(
                lambda x: x["id"] != id,
                self._members
        ))
        self._members = filtered_members
        
    def get_member(self, id: int):
        filtered_members=list(
            filter(
                lambda x: x["id"] == id,
                self._members
            )
        )
        return filtered_members.pop()


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
