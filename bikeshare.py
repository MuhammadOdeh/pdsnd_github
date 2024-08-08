import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city = input('Enter the name of the city you want to analyze (chicago, new york city, washington) : ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please enter a valid city name')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ['all', 'january', 'february', 'march', 'april','may', 'june']
    while True:
        month = input('Enter the name of the month you want to filter by (all, january, february, march, april, may, june) : ').lower()
        if month in month_name:
            break
        else:
            print('Invalid month. Please enter a valid month name')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
    while True:
        day = input('Enter the name of the day of the week you want to filter by (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) : ').lower()
        if day in day_name:
            break
        else:
            print('Invalid day. Please enter a valid day name')

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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':    
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nMost Common Month is : {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_dayOfWeek = df['day_of_week'].mode()[0]
    print('\nMost Common Day of week is : {}'.format(most_common_dayOfWeek))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour is : {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startStation = df['Start Station'].mode()[0]
    print('\nMost Common Used Start Station is : {}'.format(most_common_startStation))

    # TO DO: display most commonly used end station
    most_common_endStation = df['End Station'].mode()[0]
    print('\nMost Common Used End Station is : {}'.format(most_common_endStation))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_startEndStation_trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination_startEndStation_trip'].mode()[0]
    print('\nMost Common Combination of Start and End Station is : {}'.format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time is : {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean Travel Time is : {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types Counts : {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_ofGender = df['Gender'].value_counts()
        print('\nCounts Of Genfer : {}'.format(counts_ofGender))
    else:
        print('Gender column not found in the data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yearOfBirth = df['Birth Year'].min()
        most_recent_yearOfBirth = df['Birth Year'].max()
        most_common_yearOfBirth = df['Birth Year'].mode()[0]
        print('\nEarliest Year of Birth : {}'.format(earliest_yearOfBirth))
        print('\nMost Recent Year of Birth : {}'.format(most_recent_yearOfBirth))
        print('\nMost Common Year of Birth : {}'.format(most_common_yearOfBirth))
    else:
        print('Birth Year column not found in the data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def row_data(df):
    """Displays 5 rows of data."""
    choice = input('Enter yes if you want to display 5 rows of data: ')
    if choice != 'yes':
        return
    count = df.shape[0]
    start = 0
    # TO DO: add an interactive feature to display 5 rows of data at a time
    while True:    
        print(df[start : start + 5])
        start += 5
        if start >= count:
            break
        choice = input('Enter yes if you want to display 5 more rows of data: ')
        if choice!= 'yes':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
