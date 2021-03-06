# Alternate merged meetings solution

def merge_ranges(meetings):
    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap
        if current_meeting_start <= last_merged_meeting_end:
            # assign from the last entry in merged meetings the last_merged_meeting_start and the max of either the last_merged meeting end of the current_meeting end
            merged_meetings[-1] = last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end)

        else:
            # if there's no overlap you just add the current meeting start and end as a part of the list
            merged_meetings.append([current_meeting_start, current_meeting_end])
    # return the entire merged meetings list
    return merged_meetings
    
def merge_ranges(input_range_list):
    overlap = input_range_list[0]
    print overlap
    # last_end = overlap[-1]
    for current_start, current_end in enumerate(input_range_list[1:]):
        if last_end <= current_start:
            last_end = current_end
        else:
            overlap.append([current_start, current_end])
    return overlap

# Firecode similar question
    class Range(object):
        def __init__(self):
            self.lower_bound = -1
            self.upper_bound = -1 

        def __init__(self, lower_bound, upper_bound):
            self.lower_bound = lower_bound
            self.upper_bound = upper_bound

    def merge_ranges(input_range_list):
        # if there are no entries within input_range_list or the length is lt or equal to one 
        if input_range_list == None or len(input_range_list) <= 1:
            return input_range_list
        # set up the output list 
        output_list = []
        # previous is equal to the first entry in the input range list
        previous = input_range_list[0]
        # instantiate i at 1 since we dont need to check the first index
        i = 1
        # run this through the entire list and then break out of the while loop
        while i < len(input_range_list):
            # set current to the current index in the parameter list
            current = input_range_list[i]
            # see if there is overlap
            if previous.upper_bound >= current.lower_bound:
                # use the range class to add to the merged 
                merged = Range(previous.lower_bound, max(previous.upper_bound, current.upper_bound))
                # previous becomes merged
                previous = merged
            else:
                # add previous to the output_list if there's no overlap
                output_list.append(previous)
                # previous becomes current
                previous = current
            # increment i     
            i += 1
        # add previous to output list
        output_list.append(previous)
        # return the output list
        return output_list