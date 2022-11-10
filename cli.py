import click 
# Docs: https://click.palletsprojects.com/en/8.1.x/

from plyer import notification
import time

TITLE = "Pomodoro"

@click.command()
@click.option('--time-on', default=25.0, help="Time for studying/work in the Pomodoro session.")
@click.option('--time-off', default=5.0, help="Break time. Set to 0 for no breaks.")
@click.option('--session-count', default=4, help="Number of study sessions in the Pomodoro.")
def pomodoro(time_on, time_off, session_count) -> None: 
    if time_on==0 or session_count==0:
        click.echo(f'Invalid time periods. {time_on if time_on==0 else session_count} cannot be 0.')
        return None
    elif any(i < 0 for i in [time_on, time_off, session_count]):
        click.echo('Invalid time periods.')
        return None
    notification.notify(
        title=TITLE,
        message="Pomodoro is starting now."
    )
    for i in range(1, session_count+1):
        notification.notify(
            title=TITLE,
            message=f"Pomodoro session #{i} has started."
        )
        time.sleep(time_on*60)
        if time_off!=0:
            notification.notify(title=TITLE, message="Break has started...")
            time.sleep(time_off)

    click.echo("Congratulations, you finished your session! Hope you got something done!")
    return None

if __name__=="__main__":
    pomodoro()