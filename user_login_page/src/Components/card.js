import './card.css';

function Card({title,subtitle,img,value,color}) {

    const cardStyle = {
        backgroundColor: color // Set background color dynamically based on the color prop
    };

    return(
        <div className="card" style={cardStyle}>
            <p className='title'>{title}</p>
            <div className='img-value'>
                <img src={img} alt=''/>
                <p className='value'>{value}</p>
            </div>
            <p className='subtitle'>{subtitle}</p>
        </div>
    );

}

export default Card;
