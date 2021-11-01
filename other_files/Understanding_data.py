import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities = {'1' : 'chicago', '2' : 'new york city', '3' : 'washington'}
days = {'0' : 'all', '1' : 'Saturday', '2' : 'Sunday', '3' : 'Monday', '4' : 'Tuesday', '5' : 'Wednesday', '6' : 'Thursday', '7' : 'Friday'}
months = {'0' : 'all', '1' : 'January', '2' : 'February', '3' : 'March', '4' : 'April', '5' : 'May', '6' : 'June'}


def get_filter():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    # prompt Easy ui to user
    print("Hello! Welcome to our Explore data Program.".center(50, '*'))

    while True:

        print("1- To Start Explore Process".ljust(25), "0- To Exit Program".rjust(25))
        choosen_num = input("Enter your choice:: ")

        # check user choice to start or exit

        if choosen_num == '1':
            # Prompt an Bauty Ui to make it easy to choice filter
            while True :
                # start interact with user to make choice : city name and filter by
                print("\nWould you like to see data for Chicago, New York, or Washington?")
                print("1- To Chicago".ljust(25), "2- To New York City".center(50), "3- To Washington".ljust(25))

                # check for any input error from user and handling for city name
                try:
                    city_name = cities[str(input("Enter your Choice:: ").lower())]
                except Exception as city_name_error:
                    city_name_error = "Invalid Choice!! please choose: 1 To Chicago, 2 To New York, or 3 To Washington.".center(100,"!")
                    print(city_name_error)
                    continue
                break


            while True :

                    # prompt menu of choices to choose a month
                    print("\nWhich month - January, February, March, April, May, or June?")
                    print("1- To January".ljust(25), "2- To February".center(50), "3- To March".ljust(25))
                    print("4- To April".ljust(25), "5- To May".center(50), "6- To June".ljust(25))
                    print("0- To All Month".center(50))
                    try:
                        choice_month = months[str(input("Enter the Month Number:: ").title())]
                    except Exception as month_error:
                        month_error = "Invalid choice!! Please choose: 1, 2, 3, 4, 5 OR 6.".center(100,"!")
                        print(month_error)
                        continue

                    break

            while True:
                    # prompt menu of choices to choose a day
                    print("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
                    print("1- To Saturday".ljust(25), "2- To Sunday".center(50), "3- To Monday".ljust(25))
                    print("4- To Tuesday".ljust(25), "5- To Wednesday".center(50), "6- To Thursday".ljust(25))
                    print("7- To Friday".ljust(25), "0- To All Month".rjust(25))

                    try:
                        choice_day = days[str(input("Enter the Day Number:: "))]
                    except Exception as day_error:
                        day_error = "Invalid choice!! Please choose: 1, 2, 3, 4, 5, 6 OR 7".center(100,"!")
                        print(day_error)
                        continue
                    break

        #Exit from program
        elif choosen_num == '0':
            print("!^_^! HAVE A NICE DAY !^_^!".center(100, '#'))
            exit(0)

        else:
            print("Invalid choice!! choose from 1 OR 0".center(50,"!"))
            continue
        break
    return city_name, choice_month, choice_day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Find and Fill missing values
    while True:
        nan_found = df.isnull().sum().sum()
        if nan_found != 0:
            df.fillna(method='ffill', axis=0, inplace=True)
            continue
        else:
            break

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('Most Frequent Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('\nMost Frequent Day:', common_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('\nMost Frequent Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Frequent Start Station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most Frequent End Station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent combination of Start and End Stations: ', common_combination_station)

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The Total Travel Time: ", total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The Average Travel Time: ", avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The Counts of User Types: \n", user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print("The counts of Users Gender: \n", gender_types)


    # TO DO: Display earliest, most recent, and most common year of birth
    least_recent_year = int(df['Birth Year'].min())
    most_recent_year = int(df['Birth Year'].max())
    most_common_year = int(df['Birth Year'].value_counts().idxmax())
    print("The Earliest Year of Birth: ", least_recent_year, "\nThe most recent Year of Birth: ", most_recent_year, "\nThe most common Year of Birth: ", most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def descriptive_statistics(df):
    #See the descriptive statistics of the DataFrame
    print("The Descriptive Statistics of our DataFrame".center(100, '#'))
    print(df.describe())

def show_data_sample(df):
    print("Our DataFrame is ready !^_^!".center(100, '#'))
    while True:
        print("1- To show 5 lines of it".ljust(25), "0- To Exit".rjust(25))
        choosen_num = input("Enter your choice:: ")
        if choosen_num == '1':

            while True:
                try:
                    print(df.head())
                except Exception as e:
                    print("There's no more data to display".center(50,'!'))
                    exit(0)
                print("1- To show more 5 lines".ljust(25), "0- To Exit".rjust(25))
                num = input("Enter your choice:: ")
                if num == '1':
                    continue
                elif num == '0':
                    exit_program()
                else:
                    print("Invalid choice!! choose from 1 OR 0".center(50, "!"))
                    continue
            break
        elif choosen_num == '0':
            exit_program()
        else:
            print("Invalid choice!! choose from 1 OR 0".center(50, "!"))
            continue
        break


def exit_program():

    while True:
        print("Exploration Process Complete !^_^!".center(100, '#'))
        print("1- To Start New Explore Process".ljust(25), "0- To Exit Program".rjust(25))
        choosen_num = input("Enter your choice:: ")
        if choosen_num == '1':
            main_menu()
        elif choosen_num == '0':
            print("!^_^! HAVE A NICE DAY !^_^!".center(100, '#'))
            exit(0)
        else:
            print("Invalid choice!! choose from 1 OR 0".center(50, "!"))
            continue
        break

def main_menu():
    city, month, day = get_filter()
    df = load_data(city, month, day)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    descriptive_statistics(df)
    show_data_sample(df)


if __name__ == "__main__":
	main_menu()