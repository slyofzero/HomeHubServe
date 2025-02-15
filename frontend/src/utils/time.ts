import moment from "moment";

export function formatUnixTimestamp(
  timestamp: number | string | null | undefined
): string {
  return moment.unix(Number(timestamp)).format("Do MMM, YYYY");
}

export function timeSince(
  timestamp: number | string | null | undefined
): string {
  return moment(Number(timestamp) * 1e3).fromNow();
}
