import React from 'react';
import { Handle } from '@xyflow/react';

const CircleNode = ({ data }) => {
  return (
    <div style={{ 
        width: 50, 
        height: 50, 
        borderRadius: '50%', 
        backgroundColor: 'lightblue', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'center'
      }}>
      <Handle type="target" position="left" />
      {data.label}
      <Handle type="source" position="right" />
    </div>
  );
};

export default CircleNode;