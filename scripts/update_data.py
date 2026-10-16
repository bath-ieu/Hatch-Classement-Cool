import json
import os
import urllib.request
from datetime import datetime

SEASON_ID = "20262027"

PARTICIPANTS = [
{
"name": "Jean-Philip Tremblay",
"skaters": [8480069, 8484801, 8480839, 8480018, 8481540, 8484144, 8485366, 8477493, 8478483, 8478427, 8483445, 8484153, 8478397, 8484984, 8483515, 8484387, 8478013, 8481533, 8483495, 8478010, 8476468, 8481618],
"goalies": [8476883, 8479406, 8480045],
"teams": [8, 7, 1, 52]
},
{
"name": "Nicolas St-Pierre",
"skaters": [8480069, 8480800, 8477956, 8479318, 8477939, 8482740, 8485366, 8477493, 8478483, 8477960, 8475786, 8484153, 8477946, 8486067, 8483515, 8480893, 8478013, 8481581, 8485406, 8475168, 8484145, 8482775],
"goalies": [8476945, 8480280, 8482661],
"teams": [25, 14, 2, 28]
},
{
"name": "Alondra Rima",
"skaters": [8478402, 8484801, 8480027, 8480018, 8481557, 8478550, 8485366, 8477493, 8474578, 8478427, 8482699, 8483431, 8471215, 8484984, 8477500, 8479987, 8475754, 8481581, 8483495, 8476454, 8482702, 8481618],
"goalies": [8479979, 8479406, 8482487],
"teams": [25, 22, 2, 28]
},
{
"name": "Aya el Khazen",
"skaters": [8476453, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8481605, 8474590, 8482093, 8479343, 8473419, 8478397, 8484984, 8480830, 8481524, 8474564, 8481581, 8485391, 8476875, 8484145, 8481618],
"goalies": [8475683, 8480313, 8482487],
"teams": [8, 14, 29, 3]
},
{
"name": "Alain Roy",
"skaters": [8480069, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8477493, 8479420, 8478427, 8479314, 8480208, 8475166, 8484984, 8483515, 8484387, 8476462, 8481533, 8483495, 8478010, 8480002, 8482775],
"goalies": [8476883, 8480313, 8482487],
"teams": [21, 22, 4, 28]
},
{
"name": "Mathieu Huot",
"skaters": [8480803, 8477934, 8480839, 8480039, 8479345, 8477504, 8485366, 8481605, 8474590, 8477933, 8479343, 8476887, 8477946, 8484762, 8482078, 8481604, 8475754, 8479407, 8485406, 8482730, 8480002, 8481618],
"goalies": [8476883, 8480313, 8482661],
"teams": [21, 14, 1, 28]
},
{
"name": "Olivier Jubelin",
"skaters": [8480069, 8477934, 8478864, 8479325, 8478398, 8478550, 8485366, 8477404, 8474578, 8477933, 8479343, 8476887, 8477946, 8484227, 8477951, 8480893, 8480014, 8479407, 8483516, 8478010, 8480002, 8482775],
"goalies": [8476883, 8480313, 8474593],
"teams": [12, 7, 5, 18]
},
{
"name": "Yanick Tremblay",
"skaters": [8477492, 8483457, 8477956, 8479325, 8481540, 8480036, 8478420, 8481605, 8478483, 8480865, 8479314, 8483431, 8478397, 8484873, 8483515, 8482720, 8474564, 8477955, 8482809, 8476875, 8481598, 8481618],
"goalies": [8476945, 8480313, 8482487],
"teams": [8, 22, 26, 20]
},
{
"name": "Alexandre Neal",
"skaters": [8478402, 8483457, 8477956, 8480018, 8477939, 8471675, 8478420, 8481605, 8479420, 8480865, 8479314, 8480208, 8478038, 8484873, 8477500, 8481524, 8471214, 8478445, 8482809, 8475168, 8477346, 8478133],
"goalies": [8475683, 8479406, 8482487],
"teams": [8, 6, 26, 52]
},
{
"name": "Antoine Duguay",
"skaters": [8478402, 8480800, 8480027, 8480018, 8481540, 8482740, 8478403, 8477493, 8479420, 8480865, 8479314, 8476887, 8475166, 8484984, 8483515, 8481604, 8474564, 8477955, 8482809, 8475168, 8482702, 8481618],
"goalies": [8475683, 8478048, 8482487],
"teams": [21, 7, 26, 28]
},
{
"name": "Hakjun Oh",
"skaters": [8477492, 8484801, 8480839, 8481559, 8481540, 8478550, 8478420, 8477404, 8480801, 8476459, 8479314, 8476887, 8478397, 8486067, 8480830, 8480893, 8476462, 8481581, 8483495, 8478010, 8477346, 8482737],
"goalies": [8476883, 8475809, 8474593],
"teams": [13, 22, 1, 28]
},
]

TEAM_INFO = {
    1: {"name": "New Jersey Devils", "abbrev": "NJD"},
    2: {"name": "New York Islanders", "abbrev": "NYI"},
    3: {"name": "New York Rangers", "abbrev": "NYR"},
    4: {"name": "Philadelphia Flyers", "abbrev": "PHI"},
    5: {"name": "Pittsburgh Penguins", "abbrev": "PIT"},
    6: {"name": "Boston Bruins", "abbrev": "BOS"},
    7: {"name": "Buffalo Sabres", "abbrev": "BUF"},
    8: {"name": "Montreal Canadiens", "abbrev": "MTL"},
    9: {"name": "Ottawa Senators", "abbrev": "OTT"},
    10: {"name": "Toronto Maple Leafs", "abbrev": "TOR"},
    12: {"name": "Carolina Hurricanes", "abbrev": "CAR"},
    13: {"name": "Florida Panthers", "abbrev": "FLA"},
    14: {"name": "Tampa Bay Lightning", "abbrev": "TBL"},
    15: {"name": "Washington Capitals", "abbrev": "WSH"},
    16: {"name": "Chicago Blackhawks", "abbrev": "CHI"},
    17: {"name": "Detroit Red Wings", "abbrev": "DET"},
    18: {"name": "Nashville Predators", "abbrev": "NSH"},
    19: {"name": "St. Louis Blues", "abbrev": "STL"},
    20: {"name": "Calgary Flames", "abbrev": "CGY"},
    21: {"name": "Colorado Avalanche", "abbrev": "COL"},
    22: {"name": "Edmonton Oilers", "abbrev": "EDM"},
    23: {"name": "Vancouver Canucks", "abbrev": "VAN"},
    24: {"name": "Anaheim Ducks", "abbrev": "ANA"},
    25: {"name": "Dallas Stars", "abbrev": "DAL"},
    26: {"name": "Los Angeles Kings", "abbrev": "LAK"},
    28: {"name": "San Jose Sharks", "abbrev": "SJS"},
    29: {"name": "Columbus Blue Jackets", "abbrev": "CBJ"},
    30: {"name": "Minnesota Wild", "abbrev": "MIN"},
    52: {"name": "Winnipeg Jets", "abbrev": "WPG"},
    53: {"name": "Arizona Coyotes", "abbrev": "ARI"},
    54: {"name": "Vegas Golden Knights", "abbrev": "VGK"},
    55: {"name": "Seattle Kraken", "abbrev": "SEA"},
    59: {"name": "Utah Hockey Club", "abbrev": "UTA"},
    68: {"name": "Utah Hockey Club", "abbrev": "UTA"},
}


def fetch_json(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; NHLSuperPool/1.0)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_previous():
    previous_ranks = {}
    previous_player_pts = {}
    previous_team_pts = {}

    if not os.path.exists("data.json"):
        return previous_ranks, previous_player_pts, previous_team_pts

    try:
        with open("data.json", "r", encoding="utf-8") as f:
            old = json.load(f)
    except Exception:
        return previous_ranks, previous_player_pts, previous_team_pts

    for i, p in enumerate(old.get("leaderboard", []), start=1):
        previous_ranks[p.get("name")] = i

    for p in old.get("leaderboard", []):
        for s in p.get("skaters", []) + p.get("goalies", []):
            name = s.get("name")
            if name:
                previous_player_pts[name] = s.get("points", 0)
        for t in p.get("teams", []):
            key = t.get("abbrev") or t.get("name")
            if key:
                previous_team_pts[key] = t.get("points", 0)

    for pl in old.get("players", []):
        name = pl.get("name")
        if name and name not in previous_player_pts:
            previous_player_pts[name] = pl.get("points", 0)

    return previous_ranks, previous_player_pts, previous_team_pts


def with_pts_last(st, previous_player_pts):
    entry = dict(st)
    name = entry.get("name", "")
    current = entry.get("points", 0)
    if name in previous_player_pts:
        entry["pts_last"] = max(0, current - previous_player_pts[name])
    else:
        entry["pts_last"] = 0
    return entry


def with_team_pts_last(st, previous_team_pts):
    entry = dict(st)
    key = entry.get("abbrev") or entry.get("name", "")
    current = entry.get("points", 0)
    if key in previous_team_pts:
        entry["pts_last"] = max(0, current - previous_team_pts[key])
    else:
        entry["pts_last"] = 0
    return entry


def parse_player(pid, data):
    """Extrait les stats de la saison courante (saison régulière NHL uniquement)."""
    first = ""
    last = ""
    if isinstance(data.get("firstName"), dict):
        first = data["firstName"].get("default", "")
    else:
        first = data.get("firstName") or ""
    if isinstance(data.get("lastName"), dict):
        last = data["lastName"].get("default", "")
    else:
        last = data.get("lastName") or ""
    full_name = f"{first} {last}".strip() or f"ID {pid}"

    pos_code = data.get("position") or data.get("positionCode") or "F"
    if isinstance(pos_code, dict):
        pos_code = pos_code.get("code") or pos_code.get("default") or "F"
    pos_code = str(pos_code).upper().strip()

    if pos_code == "G":
        position = "G"
    elif pos_code == "D":
        position = "D"
    else:
        # C, L, R, W, F, etc. → attaquant
        position = "A"

    abbrev = str(
        data.get("currentTeamAbbrev")
        or data.get("teamAbbrev")
        or ""
    ).upper()

    goals = assists = points = 0
    wins = shutouts = ot_losses = 0
    found = False

    # 1) seasonTotals : saison courante + NHL + saison régulière (gameTypeId 2)
    for st in data.get("seasonTotals") or []:
        if str(st.get("season")) != SEASON_ID:
            continue
        if st.get("gameTypeId") not in (2, "2"):
            continue
        league = str(st.get("leagueAbbrev") or "NHL").upper()
        if league not in ("NHL",):
            continue

        if position == "G":
            wins = int(st.get("wins") or 0)
            shutouts = int(st.get("shutouts") or 0)
            ot_losses = int(st.get("otLosses") or st.get("overtimeLosses") or 0)
            points = wins * 4 + shutouts * 5 + ot_losses * 1
        else:
            goals = int(st.get("goals") or 0)
            assists = int(st.get("assists") or 0)
            if position == "D":
                points = goals * 3 + assists * 2
            else:
                points = goals * 2 + assists * 1
        found = True
        break

    # 2) Fallback featuredStats (uniquement si la saison affichée correspond)
    if not found:
        featured = data.get("featuredStats") or {}
        feat_season = str(featured.get("season") or "")
        if feat_season == SEASON_ID:
            # Structure réelle: featuredStats.regularSeason.subSeason
            reg = featured.get("regularSeason") or {}
            sub = reg.get("subSeason") if isinstance(reg, dict) else None
            if not isinstance(sub, dict) or not sub:
                sub = featured.get("subSeason") if isinstance(featured.get("subSeason"), dict) else {}
            if isinstance(sub, dict) and sub:
                if position == "G":
                    wins = int(sub.get("wins") or 0)
                    shutouts = int(sub.get("shutouts") or 0)
                    ot_losses = int(sub.get("otLosses") or sub.get("overtimeLosses") or 0)
                    points = wins * 4 + shutouts * 5 + ot_losses * 1
                else:
                    goals = int(sub.get("goals") or 0)
                    assists = int(sub.get("assists") or 0)
                    if position == "D":
                        points = goals * 3 + assists * 2
                    else:
                        points = goals * 2 + assists * 1
                found = True

    return {
        "id": pid,
        "name": full_name,
        "abbrev": abbrev,
        "position": position,
        "goals": goals,
        "assists": assists,
        "points": points,
        "wins": wins,
        "shutouts": shutouts,
        "otLosses": ot_losses,
    }


def main():
    previous_ranks, previous_player_pts, previous_team_pts = load_previous()

    all_skater_ids = set()
    all_goalie_ids = set()
    all_team_ids = set()
    for p in PARTICIPANTS:
        all_skater_ids.update(p["skaters"])
        all_goalie_ids.update(p["goalies"])
        all_team_ids.update(p["teams"])

    players_stats = {}

    for pid in sorted(all_skater_ids | all_goalie_ids):
        try:
            data = fetch_json(f"https://api-web.nhle.com/v1/player/{pid}/landing")
            players_stats[pid] = parse_player(pid, data)
        except Exception as e:
            print(f"Erreur joueur {pid}: {e}")
            players_stats[pid] = {
                "id": pid,
                "name": f"ID {pid}",
                "abbrev": "",
                "position": "G" if pid in all_goalie_ids else "A",
                "goals": 0,
                "assists": 0,
                "points": 0,
                "wins": 0,
                "shutouts": 0,
                "otLosses": 0,
            }

    # Index standings by team abbreviation (API no longer returns teamId reliably)
    teams_by_abbrev = {}
    try:
        standings = fetch_json("https://api-web.nhle.com/v1/standings/now")
        for t in standings.get("standings", []):
            abbrev = t.get("teamAbbrev", {})
            if isinstance(abbrev, dict):
                abbrev = abbrev.get("default", "")
            abbrev = str(abbrev or "").upper()
            if not abbrev:
                continue

            team_name = t.get("teamName", {})
            if isinstance(team_name, dict):
                team_name = team_name.get("default", abbrev)
            team_name = team_name or abbrev

            reg_wins = int(t.get("regulationWins") or 0)
            wins = int(t.get("wins") or 0)
            ot_wins = max(0, wins - reg_wins)
            ot_losses = int(t.get("otLosses") or 0)
            points = reg_wins * 3 + ot_wins * 2 + ot_losses * 1

            teams_by_abbrev[abbrev] = {
                "name": team_name,
                "abbrev": abbrev,
                "points": points,
                "reg_wins": reg_wins,
                "ot_wins": ot_wins,
                "ot_losses": ot_losses,
            }
        print(f"Standings chargés: {len(teams_by_abbrev)} équipes")
    except Exception as e:
        print(f"Erreur standings: {e}")

    # Map numeric team IDs used in PARTICIPANTS → stats via TEAM_INFO abbrev
    teams_stats = {}
    for tid in all_team_ids:
        info = TEAM_INFO.get(tid, {"name": f"Équipe {tid}", "abbrev": ""})
        abbrev = (info.get("abbrev") or "").upper()
        if abbrev and abbrev in teams_by_abbrev:
            teams_stats[tid] = dict(teams_by_abbrev[abbrev])
        else:
            teams_stats[tid] = {
                "name": info["name"],
                "abbrev": abbrev,
                "points": 0,
                "reg_wins": 0,
                "ot_wins": 0,
                "ot_losses": 0,
            }
            if abbrev:
                print(f"Attention: pas de standings pour {abbrev} (id {tid})")

    leaderboard = []

    for p in PARTICIPANTS:
        att_pts = def_pts = goalie_pts = team_pts = 0
        skater_details = []
        goalie_details = []
        team_details = []

        for pid in p["skaters"]:
            st = players_stats.get(
                pid,
                {
                    "id": pid,
                    "name": f"ID {pid}",
                    "abbrev": "",
                    "points": 0,
                    "goals": 0,
                    "assists": 0,
                    "position": "A",
                },
            )
            st = with_pts_last(st, previous_player_pts)
            if st.get("position") == "D":
                def_pts += st.get("points", 0)
            else:
                att_pts += st.get("points", 0)
            skater_details.append(st)

        for pid in p["goalies"]:
            st = players_stats.get(
                pid,
                {
                    "id": pid,
                    "name": f"ID {pid}",
                    "abbrev": "",
                    "points": 0,
                    "wins": 0,
                    "shutouts": 0,
                    "otLosses": 0,
                    "position": "G",
                },
            )
            st = with_pts_last(st, previous_player_pts)
            goalie_pts += st.get("points", 0)
            goalie_details.append(st)

        for tid in p["teams"]:
            st = teams_stats.get(tid)
            if st is None:
                info = TEAM_INFO.get(tid, {"name": f"Équipe {tid}", "abbrev": ""})
                st = {
                    "name": info["name"],
                    "abbrev": info.get("abbrev", ""),
                    "points": 0,
                    "reg_wins": 0,
                    "ot_wins": 0,
                    "ot_losses": 0,
                }
            st = with_team_pts_last(st, previous_team_pts)
            team_pts += st.get("points", 0)
            team_details.append(st)

        total_points = att_pts + def_pts + goalie_pts + team_pts

        leaderboard.append(
            {
                "name": p["name"],
                "total_points": total_points,
                "att_pts": att_pts,
                "def_pts": def_pts,
                "goalie_pts": goalie_pts,
                "team_pts": team_pts,
                "skaters": skater_details,
                "goalies": goalie_details,
                "teams": team_details,
            }
        )

    leaderboard.sort(key=lambda x: x["total_points"], reverse=True)

    for new_rank, p in enumerate(leaderboard, start=1):
        old_rank = previous_ranks.get(p["name"])
        if old_rank is None or old_rank == new_rank:
            p["trend"] = "same"
        elif new_rank < old_rank:
            p["trend"] = "up"
        else:
            p["trend"] = "down"

    seen = {}
    for entry in leaderboard:
        for s in entry.get("skaters", []):
            key = s.get("id") if s.get("id") is not None else s.get("name")
            if key is not None and key not in seen:
                seen[key] = s
        for g in entry.get("goalies", []):
            key = g.get("id") if g.get("id") is not None else g.get("name")
            if key is not None and key not in seen:
                seen[key] = g
    players_unique = list(seen.values())

    output = {
        "season": SEASON_ID,
        "updated_at": datetime.now().astimezone().isoformat(),
        "leaderboard": leaderboard,
        "players": players_unique,
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"OK — {len(leaderboard)} participants, {len(players_unique)} joueurs uniques → data.json")


if __name__ == "__main__":
    main()
