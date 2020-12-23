from part1 import seat_ids

sorted_seat_ids = sorted(seat_ids)
last_seat_ids_index = len(sorted_seat_ids) - 1
current_index = 0
seat_id = None
while current_index < last_seat_ids_index - 1:
    if sorted_seat_ids[current_index + 1] - sorted_seat_ids[current_index] == 2:
        seat_id = sorted_seat_ids[current_index] + 1
        break
        
    current_index += 1
    
print(seat_id)
