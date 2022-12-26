import random

import factory
from factory import Faker


class PlanFactory(factory.DictFactory):
    original_id = Faker("bothify", text="##?###?#")
    talent_id = Faker("bothify", text="tln_####")
    talent_name = Faker("name")
    talent_grade = Faker("first_name")
    booking_grade = Faker("first_name")
    operating_unit = Faker("bothify", text="Operating Unit #")
    office_city = Faker("city")
    office_postal_code = Faker("postcode")
    job_manager_name = Faker("name")
    job_manager_id = Faker("bothify", text="tln_####")
    total_hours = 32.0
    start_date = Faker("date_time_this_year")
    end_date = Faker("date_time_this_year")
    client_name = Faker("name")
    client_id = Faker("bothify", text="cl_####")
    industry = Faker("bothify", text="??????????")
    required_skills = random.choice([[{"name": "French", "category": "Language"}], []])
    optional_skills = random.choice(
        [[{"name": "React", "category": "Coding Language"}], []]
    )
    is_unassigned = random.choice([True, False])


if __name__ == "__main__":
    dtaa = PlanFactory()
    print(dtaa)
