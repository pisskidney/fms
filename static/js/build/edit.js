var PreviewHeader = React.createClass({
    displayName: "PreviewHeader",

    render: function () {
        return React.createElement(
            "div",
            { id: "edit-preview-header" },
            React.createElement(
                "div",
                { className: "row" },
                React.createElement(
                    "div",
                    { className: "medium-2 medium-offset-2 columns" },
                    React.createElement("a", { className: "logo", href: "/" })
                ),
                React.createElement(
                    "div",
                    { id: "header-links", className: "medium-6 columns text-right end" },
                    React.createElement(
                        "a",
                        { id: "button-help", href: "#" },
                        "Help"
                    ),
                    React.createElement(
                        "a",
                        { href: "#", className: "lightgrey" },
                        "Sign Up"
                    ),
                    React.createElement(
                        "a",
                        { href: "#", className: "lightgrey" },
                        "Log In"
                    )
                )
            )
        );
    }
});

var Preview = React.createClass({
    displayName: "Preview",

    render: function () {
        return React.createElement(
            "div",
            { className: "columns medium-10" },
            React.createElement(PreviewHeader, null),
            "preview"
        );
    }
});

var OptionLayout = React.createClass({
    displayName: "OptionLayout",

    render: function () {
        return React.createElement(
            "li",
            null,
            this.props.name
        );
    }
});

var OptionLayoutBox = React.createClass({
    displayName: "OptionLayoutBox",

    render: function () {
        return React.createElement(
            "ul",
            { className: "medium-block-grid-2" },
            React.createElement(OptionLayout, { name: "1" }),
            React.createElement(OptionLayout, { name: "2" }),
            React.createElement(OptionLayout, { name: "3" }),
            React.createElement(OptionLayout, { name: "4" }),
            React.createElement(OptionLayout, { name: "5" })
        );
    }
});

var Sidebar = React.createClass({
    displayName: "Sidebar",

    render: function () {
        return React.createElement(
            "div",
            { className: "columns medium-2" },
            React.createElement(
                "ul",
                { className: "accordion", "data-accordion": true },
                React.createElement(
                    "li",
                    { className: "accordion-navigation" },
                    React.createElement(
                        "a",
                        { href: "#panel1a" },
                        "Accordion 1"
                    ),
                    React.createElement(
                        "div",
                        { id: "panel1a", className: "content active" },
                        React.createElement(OptionLayoutBox, null)
                    )
                ),
                React.createElement(
                    "li",
                    { className: "accordion-navigation" },
                    React.createElement(
                        "a",
                        { href: "#panel2a" },
                        "Accordion 2"
                    ),
                    React.createElement(
                        "div",
                        { id: "panel2a", className: "content" },
                        "Panel 2. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    )
                ),
                React.createElement(
                    "li",
                    { className: "accordion-navigation" },
                    React.createElement(
                        "a",
                        { href: "#panel3a" },
                        "Accordion 3"
                    ),
                    React.createElement(
                        "div",
                        { id: "panel3a", className: "content" },
                        "Panel 3. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    )
                )
            )
        );
    }
});

var EditorBox = React.createClass({
    displayName: "EditorBox",

    render: function () {
        return React.createElement(
            "div",
            { className: "row" },
            React.createElement(Sidebar, null),
            React.createElement(Preview, null)
        );
    }
});

ReactDOM.render(React.createElement(EditorBox, null), document.getElementById('editor'));