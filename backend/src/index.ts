import express from "express";
import cors from "cors";
import { config } from "./config.js";
import { contactRouter } from "./routes/contact.js";
import { newsletterRouter } from "./routes/newsletter.js";
import { inquiryRouter } from "./routes/inquiry.js";
import { careerRouter } from "./routes/career.js";

const app = express();

app.use(cors({
  origin: [
    "http://localhost:5173",
    "https://digiscale-gamma.vercel.app",
    "https://digiscaleinfotech.com",
    "https://www.digiscaleinfotech.com",
  ],
  credentials: true,
  methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
  allowedHeaders: ["Content-Type", "Authorization"],
}));

app.use(express.json());

// Routes
app.use("/contact", contactRouter);
app.use("/newsletter", newsletterRouter);
app.use("/inquiry", inquiryRouter);
app.use("/career", careerRouter);

app.get("/", (req, res) => {
  res.json({
    status: "ok",
    message: `${config.APP_NAME} Running 🚀`,
  });
});

app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
  });
});

app.listen(config.PORT, () => {
  console.log(`Server running on port ${config.PORT} 🚀`);
});
