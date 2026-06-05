import { readFile } from "node:fs/promises";
import path from "node:path";
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const assignment = request.nextUrl.searchParams.get("assignment");

  if (!assignment || !/^[a-z0-9]+$/i.test(assignment)) {
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
