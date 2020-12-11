require('./tracing');
const express = require("express");
const bodyParser = require("body-parser");
const user = require("./routes/user");
const InitiateMongoServer = require("./config/db");

// Initiate Mongo Server
InitiateMongoServer();

const app = express();

// PORT
const PORT = process.env.PORT || 8080;

// Middleware
app.use(bodyParser.json());

app.get("/", (req, res) => {
    res.json({ message: "Authentication API Working" });
});

app.use("/user", user);

app.listen(PORT, (req, res) => {
    console.log(`Server Started at PORT ${PORT}`);
});