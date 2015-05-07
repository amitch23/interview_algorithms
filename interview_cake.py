"""
You've built an in-flight entertainment system
with on-demand movie streaming.

Users on longer flights like to start a second movie
 right when their first one ends, but they complain
 that the plane usually lands before they can see the ending.
 So you're building a feature for choosing two movies
 whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length
 (in minutes) and an array of integers movie_lengths
 (in minutes) and returns a boolean indicating whether
  there are two numbers in movie_lengths whose sum equals
  flight_length.

When building your function:

-Assume your users will watch exactly two movies
-Don't make your users watch the same movie twice
-Optimize for runtime over memory

"""

# Interview cake, yet again tackling the pressing problems of our day and age.

flight_length = 180
movie_lengths = [60, 90, 120, 63, 100, 90]

#poor runtime: nested for loop, check each sum
def can_watch_two_movies(flight_length, movie_lengths):

    movie_sums=[]

    for movie in movie_lengths:
        for m in range(len(movie_lengths)/2):

            if (movie_lengths[m] + movie == flight_length) and (movie_lengths[m] != movie): #assuming same length indicates same movie, faulty logic really....
                movie_sums.append((movie_lengths[m], movie))
            else:
                continue

    if movie_sums:
        return True
    else:
        return False

def can_watch_two_movies_faster(flight_length, movie_lengths):

    #put movie_lengths in a dictionary that looks like one of the following? But still would have to compare each item. Maybe a dictionary isn't useful here....
    {'1': 90, '2':97, '3': 120}
    {'90': 90, '97': 97, '120': 120}

    #or some sort algorithm? bubble? quick? merge?
    #binary tree? oh boy.







