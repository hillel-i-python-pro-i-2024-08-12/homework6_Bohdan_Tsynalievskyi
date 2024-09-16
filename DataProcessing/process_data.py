import random
from dataclasses import dataclass, field
from typing import TypeAlias, TypedDict

from faker import Faker

T_GROUP_NAME: TypeAlias = str
T_GROUP_NAMES: TypeAlias = list[T_GROUP_NAME]

T_USER_NAME: TypeAlias = str


class Human(TypedDict):
    name: T_USER_NAME
    group: T_GROUP_NAME


T_HUMANS: TypeAlias = list[Human]
T_ORGANIZED_DATA: TypeAlias = dict[str, list]
T_OUTPUT: TypeAlias = str


class Group(TypedDict):
    name: T_GROUP_NAME
    members: T_HUMANS


@dataclass
class DataProvider:
    _faker: Faker = field(default_factory=Faker)

    def _generate_group_names(
        self,
        amount: int = 10,
    ) -> T_GROUP_NAMES:
        return [self._faker.unique.company() for _ in range(amount)]

    def _generate_human(self, group_name: T_GROUP_NAME) -> Human:
        return Human(
            name=self._faker.unique.first_name(),
            group=group_name,
        )

    def _generate_humans(
        self,
        groups: T_GROUP_NAMES,
        amount_of_humans: int,
    ) -> T_HUMANS:
        members = []
        for _ in range(amount_of_humans):
            group_name = random.choice(groups)
            group_member = self._generate_human(group_name=group_name)
            members.append(group_member)

        return members

    def generate_group_members(
        self,
        amount_of_groups: None | int = None,
        amount_of_humans: None | int = None,
    ) -> T_HUMANS:
        amount_of_groups = amount_of_groups or random.randint(5, 10)
        amount_of_humans = amount_of_humans or random.randint(3, 30)

        _groups = self._generate_group_names(amount=amount_of_groups)
        return self._generate_humans(
            groups=_groups,
            amount_of_humans=amount_of_humans,
        )


def organize_data(humans: T_HUMANS) -> T_ORGANIZED_DATA:
    """
    Organize data in way, useful for further processing.
    At this stage is not allowed to make output string.
    """
    groups = {}
    for human in humans:
        group_name = human["group"]
        if group_name not in groups:
            groups[group_name] = []
        groups[group_name].append(human["name"])
    return groups


def get_formatted_output(data: T_ORGANIZED_DATA) -> T_OUTPUT:
    """
    Get output string. That can be used to print in console.
    """
    output = ""
    for group_name, members in data.items():
        s_letter = "s" if len(members) > 1 else ""
        output += (
            f"{group_name} has {len(members)} member{s_letter} "
            f"with the following name{s_letter}: {members}\n"
        )

    return output
