import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february','march', 'april','may','june']
days = ['sunday', 'monday', 'tuesday', 'wednesday','thuresday','friday', 'saturday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?: ").lower()
        if city in CITY_DATA:
            break
        else:
            print("invalid city input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month do you want to see data for? Or you can enter 'all' for the whole data: ").lower()
        if month in months:
            break
        else:
            print("invalid month input")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day of the week do you want to see data for? Or you can enter 'all' for the whole data: ").lower()
        if day in days:
            break
        else:
            print("invalid day input")
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month) + 1
        #df = df [df['Start Time'].dt.month == months]
    
    if day != 'all':
        #df = df [df['Start Time'].dt.day_name() == day.title()]
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    co_mnth= df['Start Time'].dt.month.mode()[0]

    # TO DO: display the most common day of week
    co_day= df['Start Time'].dt.day_name().mode()[0]

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    co_hr = df['hour'].mode()[0]
    
    print(f"The Most common month: {co_mnth}")
    print(f"The Most common day of week: {co_day}")
    print(f"The Most common start hour: {co_hr}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    co_used_srt_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    co_used_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Time Combination'] = df['Start Station']+ " to " + df['End Station']
    strt_end_combination = df['Start End Time Combination'].mode()[0]
    print(f"The Most common start and end combination: {strt_end_combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTraveTime = df['Trip Duration'].sum()
    print(f"Total travel time: {totalTraveTime} seconds")

    # TO DO: display mean travel time
    MeanTraveTime = df['Trip Duration'].mean()
    print(f"Mean travel time: {MeanTraveTime} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserType = df['User Type'].value_counts()
    print(f"User Type: {UserType}")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender= df['Gender'].value_counts()
        print(f"Gender: {Gender}")
    else:
        print("No inofrmation about gender available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        ear = int(df['Birth Year'].min())
        most = int(df['Birth Year'].max())
        comm_BY = int(df['Birth Year'].mode()[0])
        print(f"The earliest common year of birth: {ear}")
        print(f"The most recent common year of birth: {most}")
        print(f"The most common year of birth: {comm_BY}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """Displays 5 rows from Data Table as per user request."""
    strt = 0
    while True:
        data_table = input(("Would you like to see 5 table data for the chosen city? Enter Yes or No: ").lower())
        if data_table != 'yes' and data_table != 'no':
            print("Invalid input")
        elif data_table != 'yes':
            break
        else:
            end = strt + 5
            table = df.iloc[strt:end]
            strt += 5
            print(table)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
