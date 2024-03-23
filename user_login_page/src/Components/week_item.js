import './week_item.css';

function WeekItem({Day, In , Out , Hour}) {
    return (
        <div className="week-item">
            <p className="week-item-day">
                {Day}
            </p>
            <div className='week_value_div'>
                <p className="week-item-in">
                    {In}
                </p>
                <p className="week-item-out">
                    {Out}
                </p>
                <p className="week-item-hour">
                    {Hour}
                </p>
            </div>
        </div>
    );
}


export default WeekItem;