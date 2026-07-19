import time
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

MONTHS = ["january", "february", "march", "april", "may", "june", "all"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]


def get_filters():
    """Asks user to specify a city, month, and day to analyze"""
    print("Hello! Let's explore some US bikeshare data!")

    city = ""
    while city not in CITY_DATA:
        city = input("Which city would you like to explore: Chicago, New York City, or Washington? ").lower()

    month = ""
    while month not in MONTHS:
        month = input("Which month? January, February, March, April, May, June, or 'all'? ").lower()

    day = ""
    while day not in DAYS:
        day = input("Which day of the week? Or 'all'? ").lower()

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    if month != "all":
        month_index = MONTHS.index(month) + 1
        df = df[df["month"] == month_index]

    if day != "all":
        df = df[df["day_of_week"].str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    most_common_month = df["month"].mode()[0]
    print(f"Most common month: {most_common_month}")

    most_common_day = df["day_of_week"].mode()[0]
    print(f"Most common day of week: {most_common_day}")

    most_common_hour = df["hour"].mode()[0]
    print(f"Most common start hour: {most_common_hour}")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    most_common_start = df["Start Station"].mode()[0]
    print(f"Most common start station: {most_common_start}")

    most_common_end = df["End Station"].mode()[0]
    print(f"Most common end station: {most_common_end}")

    df["trip"] = df["Start Station"] + " -> " + df["End Station"]
    most_common_trip = df["trip"].mode()[0]
    print(f"Most common trip: {most_common_trip}")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    total_travel_time = df["Trip Duration"].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    mean_travel_time = df["Trip Duration"].mean()
    print(f"Average travel time: {mean_travel_time:.2f} seconds")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    user_types = df["User Type"].value_counts()
    print("Counts of user types:")
    print(user_types.to_string())

    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print("\nCounts of gender:")
        print(gender_counts.to_string())
    else:
        print("\nGender data not available for this city.")

    if "Birth Year" in df.columns:
        print(f"\nEarliest birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")
    else:
        print("Birth year data not available for this city.")

    print(f"\nThis took {time.time() - start_time:.4f} seconds.")
    print("-" * 40)


def raw_data(df):
    """Displays 5 rows of raw data at a time, if the user wants to see it."""
    row = 0
    show = input("Would you like to see 5 rows of raw data? Enter yes or no. ").lower()
    while show == "yes":
        print(df.iloc[row:row + 5])
        row += 5
        show = input("Would you like to see 5 more rows? Enter yes or no. ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n").lower()
        if restart != "yes":
            break


if __name__ == "__main__":
    main()
