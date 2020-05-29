
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
        self._members = [

                        {"id":"1", "_name":"John","last_name":"Jackson", "age":"3"},
                        {"id":"2", "_name":"Doe","last_name":"Jackson", "age":"55"},
                        {"id":"3", "_name":"Teresa","last_name":"Jackson", "age":"33"}

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member = {
                "id":generateId(),
                 "name": member._name,
                "lastname": memeber.last_name,
                "age": member.age
        }
        
        self._members.append(member)
        return(member)

    def delete_member(self, id):
        # fill this method and update the return
        member = self.get_member(id)
        member.remove()
                
        

    def get_member(self, id):
        member = list(filter(lambda item: item["id"]==id, self._members))
        return (member)

        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
