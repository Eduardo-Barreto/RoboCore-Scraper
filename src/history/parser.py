from .models import Match, Event, Robot


def extract_robot_data(soup, robot_id):
    robot_name = soup.find("h2").text.strip().replace("score history", "")
    robot_team = soup.find("p").text.strip()
    robot_category = soup.find("p", style="color: gray;").text.strip()

    return Robot(robot_id, robot_name, robot_team, robot_category, [])


def extract_event_data(event, robot_name, event_id):
    event_name = event.find("h3").text.split("\n")[0].strip()

    ul_items = event.find("ul").find_all("li")
    event_location = ul_items[0].text.strip()
    event_start_date, event_end_date = ul_items[1].text.split(" - ")

    event_start_date = event_start_date.strip("\t")
    event_end_date = event_end_date.strip("\t")

    matches = extract_matches(event, robot_name)
    return Event(
        event_id, event_name, event_location, event_start_date, event_end_date, matches
    )


def extract_matches(event, robot_name):
    matches = event.find("tbody").find_all("tr")

    extracted_matches = []

    for match in matches:
        result = match.find_all("td")[1]
        opponent = " ".join(result.text.split()[2:])
        opponent_id = match.find("a")["href"].replace("/history/", "")
        winner = robot_name if "won" in result.text.lower() else opponent

        extracted_matches.append(Match(opponent, opponent_id, winner))

    return extracted_matches
