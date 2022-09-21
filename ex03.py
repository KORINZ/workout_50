#calculate the average time for a user to run 10 km.

def run_timing():

	run_count = 0
	total_time = 0
	run_time_average = 0

	while True:

		run_time = input('Enter 10 km run time in minutes (press ENTER key to exit): ')

		if not run_time:
			break

		total_time += float(run_time)
		run_count += 1

		run_time_average = total_time/run_count
			
	return print(f'Average of {run_time_average}, ', f'over {run_count} runs.')

run_timing()