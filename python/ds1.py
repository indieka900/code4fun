def longest_message_streak(messages):
    # Handle empty or invalid input
    if not messages or not isinstance(messages, str):
        return 0
        
    max_streak = 0
    current_streak = 0
    current_status = None
    
    # Map each status to its progression level
    status_level = {'S': 0, 'D': 1, 'R': 2}
    
    for i, msg in enumerate(messages):
        print(i , msg)
        # Skip invalid characters
        if msg not in status_level:
            current_streak = 0
            current_status = None
            continue
            
        if current_status is None:
            # Starting a new streak
            current_streak = 1
            current_status = msg
        else:
            current_level = status_level[current_status]
            new_level = status_level[msg]
            
            if new_level == current_level:
                # Same status - extend streak
                current_streak += 1
            elif new_level > current_level:
                # Valid progression - extend streak
                current_streak += 1
            elif new_level < current_level:
                # Invalid progression - check if this can start a new streak
                if i + 2 < len(messages):
                    # Look ahead to see if we should start new streak here
                    max_streak = max(max_streak, current_streak)
                    current_streak = 1
                else:
                    # Not enough characters left for a longer streak
                    max_streak = max(max_streak, current_streak)
                    current_streak = 0
            
            current_status = msg
            
    # Check final streak
    max_streak = max(max_streak, current_streak)
    
    return max_streak

# Test cases
test_cases = [
    "SDRSDRSDRSDR",  # Should return 3
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {longest_message_streak(test)}\n")