export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOME', 'Union Square'];

  this.addNeighborhood = (newNeighborhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighborhood);
    return this.sanFranciscoNeighborhoods;
  };
}
