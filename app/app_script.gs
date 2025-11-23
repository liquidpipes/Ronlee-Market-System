/**
 * app_script.gs
 *
 * Google Apps Script to pull Fusion+ JSON from the worker endpoint
 * and write it into a Google Sheet.
 */

const FUSION_ENDPOINT = "https://your-worker-domain.workers.dev";
const SHEET_NAME = "radar";

function fetchFusionForSymbol(symbol) {
  const url = `${FUSION_ENDPOINT}?symbol=${encodeURIComponent(symbol)}`;
  const response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  const status = response.getResponseCode();

  if (status !== 200) {
    throw new Error(`Fusion endpoint error (${status}): ${response.getContentText()}`);
  }

  const data = JSON.parse(response.getContentText());
  return data;
}

function appendFusionRow(symbol) {
  const sheet = SpreadsheetApp.getActive().getSheetByName(SHEET_NAME);
  if (!sheet) {
    throw new Error(`Sheet "${SHEET_NAME}" not found.`);
  }

  const data = fetchFusionForSymbol(symbol);

  const row = [
    new Date(),
    data.symbol,
    data.fusion_score,
    data.decision,
    data.components.cf,
    data.components.dsg,
    data.components.sd,
    data.components.pc,
  ];

  sheet.appendRow(row);
}

function runFusionDigest() {
  const sheet = SpreadsheetApp.getActive().getSheetByName(SHEET_NAME);
  if (!sheet) {
    throw new Error(`Sheet "${SHEET_NAME}" not found.`);
  }

  const values = sheet.getRange("A2:A").getValues();
  for (let i = 0; i < values.length; i++) {
    const symbol = (values[i][0] || "").toString().trim();
    if (!symbol) continue;
    appendFusionRow(symbol);
  }
}
