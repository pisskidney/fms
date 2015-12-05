var PreviewHeader = React.createClass({
    render: function() {
        return (
            <div id="edit-preview-header">
                <div className="row">
                    <div className="medium-2 medium-offset-2 columns">
                        <a className="logo" href="/"></a>  
                    </div>
                    <div id="header-links" className="medium-6 columns text-right end">
                        <a id="button-help" href="#">Help</a>
                        <a href="#" className="lightgrey">Sign Up</a>
                        <a href="#" className="lightgrey">Log In</a>
                    </div>
                </div>
            </div>
        );
    }
});


var Preview = React.createClass({
    render: function() {
        return (
            <div className="columns medium-10">
                <PreviewHeader />
                preview     
            </div>
        );
    }
});

var OptionLayout = React.createClass({
    render: function () {
        return (
            <li>{this.props.name}</li>
        );
    }
});

var OptionLayoutBox = React.createClass({
    render: function () {
        return (
            <ul className="medium-block-grid-2">
                <OptionLayout name="1" />
                <OptionLayout name="2" />
                <OptionLayout name="3" />
                <OptionLayout name="4" />
                <OptionLayout name="5" />
            </ul>
        );
    }
});

var Sidebar = React.createClass({
  render: function() {
    return (
        <div className="columns medium-2">
            <ul className="accordion" data-accordion>
            <li className="accordion-navigation">
                <a href="#panel1a">Accordion 1</a>
                <div id="panel1a" className="content active">
                    <OptionLayoutBox />
                </div>
            </li>
            <li className="accordion-navigation">
                <a href="#panel2a">Accordion 2</a>
                <div id="panel2a" className="content">
                Panel 2. Lorem ipsum dolor sit amet, consectetur adipisicing
                elit, sed do eiusmod tempor incididunt ut labore et dolore
                magna aliqua. Ut enim ad minim veniam, quis nostrud
                exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat.
                </div>
            </li>
            <li className="accordion-navigation">
                <a href="#panel3a">Accordion 3</a>
                <div id="panel3a" className="content">
                Panel 3. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </div>
            </li>
            </ul>
        </div>
    );
  }
});

var EditorBox = React.createClass({
  render: function() {
    return (
        <div className="row">
            <Sidebar />
            <Preview />
        </div>
    );
  }
});

ReactDOM.render(
  <EditorBox />,
  document.getElementById('editor')
);
