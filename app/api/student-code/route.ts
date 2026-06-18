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

  const assignmentDir = path.join(process.cwd(), "assignments", assignment);
  const codePath = path.join(assignmentDir, "student_code.py");
  const testPath = path.join(assignmentDir, "test_assignment.py");

  let code: string;
  try {
    code = await readFile(codePath, "utf8");
  } catch {
    return NextResponse.json({ error: "Assignment file not found" }, { status: 404 });
  }

  // The unit tests decide whether an assignment unlocks, so ship them too.
  // A missing test file is not fatal — the client treats it as "locked".
  let testCode: string | null = null;
  try {
    testCode = await readFile(testPath, "utf8");
  } catch {
    testCode = null;
  }

  return NextResponse.json({ assignment, code, testCode });
}
