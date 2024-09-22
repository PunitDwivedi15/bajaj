const express = require('express');
const app = express();
const cors = require("cors");
app.use(express.json());
app.use(cors());

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Sample user data
const userData = {
    user_id: "john_doe_17091999",
    email: "john@xyz.com",
    roll_number: "ABCD123"
};

// POST /bfhl
app.post('/bfhl', (req, res) => {
    const { data } = req.body;

    if (!Array.isArray(data)) {
        return res.status(400).json({ is_success: false, message: "Invalid input" });
    }

    const numbers = data.filter(item => !isNaN(item));
    const alphabets = data.filter(item => /^[a-zA-Z]$/.test(item));
    const highestAlphabet = alphabets.length ? [alphabets.sort().pop()] : [];

    const response = {
        is_success: true,
        ...userData,
        numbers,
        alphabets,
        highest_alphabet: highestAlphabet
    };

    res.json(response);
});

// GET /bfhl
app.get('/bfhl', (req, res) => {
    res.status(200).json({
        operation_code: 1
    });
});
