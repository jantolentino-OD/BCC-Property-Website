// =========================================================
// Brightside Collective — "Just Breathe" Lakehouse & Cabin
// Site behavior: booking form -> redirect to Airbnb listing
// =========================================================

const AIRBNB_ROOM_ID = "1700920630627960397";

function goToAirbnb(e) {
  e.preventDefault();
  const checkin = document.getElementById('checkin').value;
  const checkout = document.getElementById('checkout').value;
  const guests = document.getElementById('guests').value || 2;

  let url = "https://www.airbnb.com/rooms/" + AIRBNB_ROOM_ID +
    "?adults=" + encodeURIComponent(guests);

  if (checkin) url += "&check_in=" + checkin;
  if (checkout) url += "&check_out=" + checkout;

  window.open(url, "_blank", "noopener");
  return false;
}
