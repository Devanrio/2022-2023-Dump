function Header(){
    return (
        <div class="header">
            <h1>Vinita Patricia</h1>
            <p>1234 Main Street, Sometown, CA 93829<br/>instagram: <a href = "https://www.instagram.com/abcdefghi__lmnopqrstuvwxyz/" target="_blank">abcdefjhi__lmnopqrstuvwxyz</a>, email:<a href = "mailto:vinitapatricia@mail.com">vinitapatricia@mail.com</a><br/>twitter:<a href="https://twitter.com/BTS_twt" target="_blank">vinitaaa</a></p>

        </div>
    )
}

function Section1(){
    return (
        <div class="section1">
            <aside>
            </aside>
            
            <h2 class = "category-label">summary of qualificattion</h2>
            <ul>
                <li><a href="https://i.pinimg.com/736x/83/56/29/8356297818b132313937cec166923f4e.jpg" target="_blank">IELTS certificate</a></li>
                <li>
                    Highly skilled and dedicated professional offering a solid background in whatever it is you need
                </li>
                <li>
                    Provide comp ..
                </li>
                <li>Computer proficient...</li>
            </ul>
        </div>
    )
}

function Section2(){
    <div class="section2">
        <h2 class = "category-label">professional experience</h2>
        <div class="indented-text">
            <h3>Operations Manager, Super Awesome Company</h3>
            <ul>
                <li>Direct all department</li>
                <li>Coordinate with ...</li>
                <li>Generally in charge of everything</li>
            </ul>

            <h3>Operations Manager, Super Awesome Company</h3>
            <ul>
                <li>Direct all department</li>
                <li>Coordinate with ...</li>
                <li>Generally in charge of everything</li>
            
            </ul>
        </div>
    </div>
}

ReactDOM.render(
    <div>
        <Header />
        <Section1 />
        <Section2 />
    </div>,
    document.getElementById('root')
);