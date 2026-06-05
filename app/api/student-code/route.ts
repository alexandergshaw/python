import { readFile } from "node:fs/promises";
import path from "node:path";
import { NextRequest, NextResponse } from "next/server";

const ALLOWED_ASSIGNMENTS = new Set([
  "assignment0",
  "assignment1",
  "assignment2",
  "assignment3",
  "review1",
  "exam1",
  "assignment4",
  "assignment5",
  "assignment6",
  "assignment7",
  "assignment8",
  "assignment9",
  "assignment10",
  "review2",
  "exam2",
  "final",
]);

export async function GET(request: NextRequest) {
  const assignment = request.nextUrl.searchParams.get("assignment");

  if (!assignment || !ALLOWED_ASSIGNMENTS.has(assignment)) {
    return NextResponse.json({ error: "Invalid assignment value" }, { status: 400 });
  }

  const filePath = path.join(process.cwd(), "assignments", assignment, "student_code.py");

  try {
    const code = await readFile(filePath, "utf8");
    return NextResponse.json({ assignment, code });
  } catch {
    return NextResponse.json({ error: "Assignment file not found" }, { status: 404 });
  }
}
