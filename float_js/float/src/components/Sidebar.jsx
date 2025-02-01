const Sidebar = ({ thoughts = [] }) => {
  // 👈 Default to empty array
  return (
    <aside className="sidebar">
      <h2>Thoughts</h2>
      <ul>
        {thoughts.map((thought, index) => (
          <li key={index}>{thought}</li>
        ))}
      </ul>
    </aside>
  );
};

export default Sidebar;
