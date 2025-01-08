def main():

    file = open("input.txt")

    # Parse input
    reports = [ [int(level) for level in line.split(" ")] for line in file.readlines() ]
    
    count, reports = safe_reports(reports)
    

    print(f"Number of safe reports, before dampening is {count}")

    count += damp_them_reports(reports)

    print(f"Number of reports, after problem dampner is {count}")
    

def safe_check(levels: list[int]):
    thresholds = [1, 2, 3]
    flag = True
    for i in range(1, len(levels)):
        diff = levels[i-1] - levels[i]

        # Check for monotonity
        if not (sorted(levels) == levels or sorted(levels, reverse = True) == levels):
            flag = False
            break

        # Checks for difference limits
        if abs(diff) not in thresholds:
            flag = False
            break

    return flag


# Part 1
def safe_reports(reports: list[list[int]]) -> int:
    
    unsafe_reports = []
    safe_count = 0
    for levels in reports:

        if safe_check(levels):
            #print(levels)
            safe_count += 1
        else:
            unsafe_reports.append(levels)

    return safe_count, unsafe_reports


# Part two, brute approach
def damp_them_reports(reports: list[list[int]]):    
    
    safe_count = 0
    for levels in reports:
        for i in range(0, len(levels)):
            ml = levels[:]
            del ml[i]
            print(ml)
            if safe_check(ml):
                safe_count += 1
                break

    return safe_count


main()
