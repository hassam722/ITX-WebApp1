import "./account.css"

function AccountDiv({username,account_img}){
    return (
        <div className="account-div">
            <p>{username}</p>
            <img src={account_img} className="account-img" alt="account-img" />
        </div>
    )
}

export default AccountDiv