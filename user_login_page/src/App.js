import logo from './logo.svg';
import AccountDiv from './Components/account';
import account_img from './Components/images/account.png';
import absent_img from './Components/images/account-outline.png';
import cash from './Components/images/cash.png';
import cash_minus from './Components/images/cash-minus.png';
import Card from './Components/card';
import Week from './Components/week';
import ButtonDiv from './Components/button_div';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className='header_div'>
        <AccountDiv username="Hassam" account_img ={account_img} className="account_div" />
      </div>
      
      <div className='cards_div'>
        <Card title="Total Presents" subtitle="This Month" img={account_img} value="20" color="#8280E9" />
        <Card title="Total Absents" subtitle="This Month" img={absent_img} value="2" color="#8280e9b3" />
        <Card title="Deduction" subtitle="This Month" img={cash_minus} value="2,000" color="#F9A4A4" />
        <Card title="Payable" subtitle="This Month" img={cash} value="20,000" color="#9FBDF8" />
        
      </div>
      <div className='week_divOrbtn_div'>
      <Week/>
      <ButtonDiv/>
      </div>
    </div>
  );
}

export default App;