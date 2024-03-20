import './week.css';
import WeekItem from './week_item';

function Week() {
    return (
        <div className="week">
            <div className="week_items">
            <WeekItem Day="Day" In="In" Out="Out" Hour='Hour' />
            <WeekItem Day="Monday" In="8:00 AM" Out="4:00 PM" Hour='08:00:00' />
            <WeekItem Day="Tuesday" In="-" Out="-" Hour='-' />
            <WeekItem Day="Wednesday" In="-" Out="-" Hour='-' />
            <WeekItem Day="Thursday" In="-" Out="-" Hour='-' />
            <WeekItem Day="Friday" In="-" Out="-" Hour='-' />
            </div>
            <div className="sub_title_div">
                <p>
                    This Week
                </p>
            </div>

        </div>
    );
}

export default Week;