# Task1: VLAN range
# На встрече написали [скрипт](/021.script.example.01/021.main.py) который
# в своей работе делает unrange списка vlan: `10,20,30-35,40` ->
# `10,20,30,31,32,33,34,35,40`.
# Нужно сделать обратную операцию по сбору подряд идущих vlan в
# диапазон: `10,20,30,31,32,33,34,35,40` -> `10,20,30-35,40`.


def unrange_vlans(vlans_str) -> list:
    result = []
    for item in vlans_str.split(","):
        if "-" in item:
            start, end = map(int, item.split("-"))
            result.extend(range(start, end + 1))
        else:
            result.append(int(item))
    return result


def range_vlans(vlans_list) -> str:
    norm_vlans = list(sorted(map(int, vlans_list)))
    result = []

    start = norm_vlans[0]
    end = norm_vlans[0]

    for vlan in norm_vlans[1:]:
        if vlan == end + 1:
            end = vlan
        else:
            if start == end:
                result.append(f"{start}")
            else:
                result.append(f"{start}-{end}")
            start = vlan
        end = vlan
    result.append(str(start) if start == end else f"{start}-{end}")
    return ",".join(result)


if __name__ == "__main__":

    sample_string = "10,20,30-35,40,50,52-55"
    sample_list = [10, 20, 30, 31, 32, 33, 34, 35, 40, 50, 52, 53, 54, 55]

    assert sample_string == range_vlans(sample_list)
    assert sample_list == unrange_vlans(sample_string)

    print(f"Sample cisco-like vlan list: {sample_string}")
    print(f"Sample unranged vlan list: {sample_list}")
    print(f"Result of `unrange_vlans`: {unrange_vlans(sample_string)}")
    print(f"Result of `range_vlans`: {range_vlans(sample_list)}")
