function Navbar(){
    return (
        <nav className="navbar navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">
                    Ignatius Global School
                </a>
            </div>
        </nav>
    )
}

function MainContent(){
    return (
        <h1>I'm Learning React!</h1>
    )
}

ReactDOM.render(
    <div>
        <Navbar />
        <MainContent />
    </div>,
    document.getElementById('root')
);