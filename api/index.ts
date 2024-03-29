import express, { Express, Request, Response } from "express";

const app: Express = express();

app.get("/", (req: Request, res: Response) => {
	return res.json(req.url);
});

app.listen(3000, () => {
	console.log("Listening on port 3000");
});
