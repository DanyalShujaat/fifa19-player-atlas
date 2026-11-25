# Player Atlas — FIFA 19 Data Explorer

A responsive, interactive exploration of 18,207 FIFA 19 player records. Search names or clubs, filter by position, nationality and rating, inspect player profiles, and compare overall rating, potential, age, and growth potential.

## Run locally

```bash
python -m http.server 8000
```

Open `http://localhost:8000`. The frontend is plain HTML, CSS, and JavaScript, with no build step.

## Data and provenance

The project uses the [FIFA 19 complete player dataset](https://www.kaggle.com/karangadiya/fifa19), mirrored [here](https://github.com/yubialam/FIFA-19-complete-player-dataset). `prepare_data.py` extracts the fields the frontend needs into `players.json`; it retains all 18,207 valid player rows. Download the original `data.csv` as `source-data.csv`, then run:

```bash
python prepare_data.py
```

The raw source CSV is excluded from this repository. The ratings are game data. Potential minus overall is used only as an exploratory comparison and is not a real-world scouting forecast.

## Project purpose

This frontend presents the original exploratory analysis as a fast, understandable experience: users can move from broad distributions to individual player records without opening a notebook.
