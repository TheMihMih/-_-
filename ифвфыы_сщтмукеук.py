from typing import Iterable


examle_1 = {"a": "1"}
result_1 = {"a": "1"}

examle_3 = ["1", "2"]
result_3 = {"0": "1", "1": "2"}

examle_4 = ["a", {"s": "1"}]
result_4 = {"0": "a", "1_s": "1"}

examle_5 = {"a": ["1", "2"]}
result_5 = {"a_0": "1", "a_1": "2"}

examle_6 = {"a": [{"b": "1"}, {"c": "2"}]}
result_6 = {"a_0_b": "1", "a_1_c": "2"}

examle_7 = {"a": {"b": "1", "c": {"d": "2"}}}
result_7 = {"a_b": "1", "a_c_d": "2"}

examle_2 = {"a": {"b": "1"}}
result_2 = {"a_b": "1"}


def badass_converter(shit_to_convert: Iterable, current_key: str = "", new_keys: list = [], result_dict: dict[str, str] = {}):

    for item in shit_to_convert:
        if isinstance(shit_to_convert, str):
            ...

        elif isinstance(shit_to_convert, list):
            ...

        elif isinstance(shit_to_convert, dict):
            new_keys = [
                f"{current_key}_{key}" if current_key else key
                for key in shit_to_convert.keys()
            ]

            for key, value in shit_to_convert.items():
                current_value = badass_converter(shit_to_convert, current_key)

            return badass_converter(shit_to_convert, key, new_keys)

    return result_dict

if __name__ == "__main__":
    print(badass_converter(examle_1))
    print(badass_converter(examle_2))
    print(badass_converter(examle_3))
    print(badass_converter(examle_4))
    print(badass_converter(examle_5))
    print(badass_converter(examle_6))
    print(badass_converter(examle_7))
