def action_based_on_traffic_signal(color):
    if color == "red":
        return "Stop"
    elif color == "yellow":
        return "Ready / Caution"
    elif color == "green":
        return "Go"
    else:
        return "Invalid color"

traffic_signal_color = input("Enter the traffic signal color (red, yellow, green): ").strip().lower()
print(action_based_on_traffic_signal(traffic_signal_color))