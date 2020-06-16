import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities_list =['chicago','new york city','washington']
#months_list variable list of months that will be used to filter the data.
months_list =['january', 'february', 'march', 'april', 'may', 'june', 'all']
days_list=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
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
        city = input("Enter name of the city ('chicago','new york city','washington') \n")
        city =city.lower()
        if city in cities_list:
            break;
        else:
            print("Please enter correct city again !!")
            continue;

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =input("Enter month ('january', 'february', 'march', 'april', 'may', 'june')  to filter by, or 'all' to apply no month filter \n")
        month=month.lower()
        if month in months_list:
            break;
        else:
            print("Please enter correct month again !!")
            continue;

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =input("Enter  day ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday') of week to filter by, or 'all' to apply no day filter \n")  
        day=day.lower()
        if day in days_list:
            break;
        else:
            print("Please enter correct day again !!")
            continue;
            
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
    # load the dataset
    df= pd.read_csv(CITY_DATA[city])
    
    #change the datatype of Start Time from object to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    #Add new column for Month
    df['Month']= df['Start Time'].dt.month
    
    #Add new column for Day
    df['Day']= df['Start Time'].dt.dayofweek
    
    if month !='all':
        month =months_list.index(month)+1
        df= df[df['Month']==month]
    if day !='all':
        day=days_list.index(day)
        df=df[df['Day']== day]
    

    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    common_month=months_list[common_month-1]
    print('The most common month is ' , common_month)

    # TO DO: display the most common day of week
    common_day = df['Day'].mode()[0]
    common_day=days_list[common_day]
    print('The most common day is ' , common_day)

    # TO DO: display the most common start hour
    df['Hour']= df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour is ' , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station is ', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\n Most Commonly used end station is ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    comb_start_end = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]

    print('\n Most Commonly used combination of start station and end station trip is', comb_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('The total travel time is ', total_time)

    # TO DO: display mean travel time
    total_mean =df['Trip Duration'].mean()
    print('The mean travel time is ', total_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('User types : \n', user_type)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender :\n', gender)
    except KeyError:
        print('\n No data available for gender\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year of birth is' , earliest_year)
    except KeyError:
        print('\n No data available for Birth Year \n')
     
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year of birth is ', most_recent_year )
    except KeyError:
        print('\n No data available for Birth Year \n')
        
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print('\nMost Common Year is ', most_common_year)
    except KeyError:
        print('\n No data available for Birth Year\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """
    Ask the user, " do you want to see raw data?" if user input yes, then it should show 5 lines of raw data. and again       it should ask the user "do you want to see more 5 lines of raw data?" if yes user yes then it should again show           further 5 line of raw data and this should be continuously going until the user gives input "No".
    
    """
    rows = 5
    start = 0
    end = rows - 1    

    
    while True:
        data = input('Do you want to see raw data (yes or no)?')
        data = data.lower()
        if data == 'yes':
            print('\n Displaying rows from  {} to {}:'.format(start + 1,end + 1))

            print('\n', df.iloc[start : end + 1])
            start += rows
            end += rows

            print('\n Do you want to see the next {} rows?'.format(rows))
            continue
        else:
            break
#Below is the main functon from where execution start
def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df)
       display_data(df) 

    
       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
